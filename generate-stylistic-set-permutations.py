import sys
import os
from itertools import combinations

sys.path.append('./pyftfeatfreeze')

from pyftfeatfreeze import RemapByOTL, parseOptions


def main():
    args = parseOptions()
    inpath = args.inpath or '.'
    outpath = args.outpath or '.'
    features = args.features.split(',')

    fonts = [
        (font, featureSet)
        for font in os.listdir(inpath)
        for length in range(len(features))
        for featureSet in combinations(features, length + 1)
    ]

    i = 0
    for font, featureSet in fonts:
        commaSeparatedFeatures = ','.join(featureSet)
        hyphenatedFeatures = '-'.join(featureSet)

        newFont = font.replace('.ttf', '-{}.ttf'.format(
            hyphenatedFeatures,
        ))

        outDir = os.path.join(outpath, hyphenatedFeatures)
        if not os.path.exists(outDir):
            os.mkdir(outDir)

        args.features = commaSeparatedFeatures
        args.usesuffix = commaSeparatedFeatures
        args.rename = True

        args.inpath = os.path.join(inpath, font)
        args.outpath = os.path.join(hyphenatedFeatures, newFont)
        if outpath:
            args.outpath = os.path.join(outpath, args.outpath)

        i += 1
        sys.stdout.write('\r{}/{} generating font {}'.format(
            i,
            len(fonts),
            args.outpath,
        ))
        sys.stdout.flush()

        RemapByOTL(args).run()

    sys.stdout.write('\n')


if __name__ == "__main__":
    finish = main()
    sys.exit(finish)
