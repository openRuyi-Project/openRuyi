# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Differences
Version:        0.72
Release:        %autorelease
Summary:        Test strings and data structures and show differences if not ok
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Differences
#!RemoteAsset:  sha256:648844b9dcb7dae6f9b5a15c9359d0f09de247a624b65c4620ebff249558f913
Source0:        https://www.cpan.org/authors/id/D/DC/DCANTRELL/Test-Differences-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.24
BuildRequires:  perl(Data::Dumper) >= 2.126
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Diff) >= 1.43

Requires:       perl(Capture::Tiny) >= 0.24
Requires:       perl(Data::Dumper) >= 2.126
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Text::Diff) >= 1.43

%description
When the code you're testing returns multiple lines, records or data
structures and they're just plain wrong, an equivalent to the Unix diff
utility may be just what's needed. Here's output from an example test
script that checks two text documents and then two (trivial) data
structures:

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
