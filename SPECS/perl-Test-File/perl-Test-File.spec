# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-File
Version:        1.995
Release:        %autorelease
Summary:        Test file attributes
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test-File
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BR/BRIANDFOY/Test-File-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder) >= 1.001006
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(version) >= 0.86

%description
This modules provides a collection of test utilities for file attributes.

%prep
%setup -q -n Test-File-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CITATION.cff INSTALL.SKIP SECURITY.md

%changelog
%autochangelog
