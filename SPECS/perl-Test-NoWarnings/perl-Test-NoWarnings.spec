# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-NoWarnings
Version:        1.06
Release:        %autorelease
Summary:        Make sure you didn't emit any warnings while testing
License:        LGPL-2.0-or-later
URL:            https://metacpan.org/dist/Test-NoWarnings
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/H/HA/HAARG/Test-NoWarnings-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder) >= 0.86
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Tester) >= 0.107

Requires:       perl(Test::Builder) >= 0.86

%description
In general, your tests shouldn't produce warnings. This modules causes any
warnings to be captured and stored. It automatically adds an extra test
that will run when your script ends to check that there were no warnings.
If there were any warnings, the test will give a "not ok" and diagnostics
of where, when and what the warning was, including a stack trace of what
was going on when the it occurred.

%prep
%setup -q -n Test-NoWarnings-%{version}

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
