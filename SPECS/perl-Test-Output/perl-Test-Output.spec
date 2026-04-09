# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Output
Version:        1.036
Release:        %autorelease
Summary:        Utilities to test STDOUT and STDERR messages
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test-Output
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BR/BRIANDFOY/Test-Output-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp) >= 0.17
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Tester) >= 0.107
BuildRequires:  perl(version) >= 0.86

Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(File::Temp) >= 0.17

%description
Test::Output provides a simple interface for testing output sent to STDOUT
or STDERR. A number of different utilities are included to try and be as
flexible as possible to the tester.

%prep
%setup -q -n Test-Output-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes INSTALL.SKIP SECURITY.md

%changelog
%autochangelog
