import re


class SemVer(object):
    'Data Type for a Semantic Version with comparison operators'

    def __init__(self, semver_string):

        self.semver_re = re.compile(
            '^([0-9]+)'
            '\.([0-9]+)'
            '\.([0-9]+)'
            '(-[0-9A-Za-z-\.]+)?'
            '(\+[0-9A-Za-z-\.]+)?$'
        )

        match = self.semver_re.match(semver_string)
        if not match:
            raise Exception('Invalid SV syntax')

        major, minor, patch, prerelease, build = list(match.groups())
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)
        self.prerelease = prerelease
        self.build = build

        self.semver_string = semver_string

    def toString(self):
        return self.semver_string

    def __gt__(self, otherSV):
        pass

    def __lt__(self, otherSV):
        pass

    def __eq__(self, otherSV):

        if

        pass
