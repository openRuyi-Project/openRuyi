# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Diff
Version:        1.45
Release:        %autorelease
Summary:        Perform diffs on files and record sets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Diff
#!RemoteAsset:  sha256:e8baa07b1b3f53e00af3636898bbf73aec9a0ff38f94536ede1dbe96ef086f04
Source0:        https://www.cpan.org/authors/id/N/NE/NEILB/Text-Diff-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:       perl(Algorithm::Diff) >= 1.19

%description
diff() provides a basic set of services akin to the GNU diff utility. It is
not anywhere near as feature complete as GNU diff, but it is better
integrated with Perl and available on all platforms. It is often faster
than shelling out to a system's diff executable for small files, and
generally slower on larger files.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
