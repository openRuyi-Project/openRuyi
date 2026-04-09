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
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DC/DCANTRELL/Test-Differences-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
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

%prep
%setup -q -n Test-Differences-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
