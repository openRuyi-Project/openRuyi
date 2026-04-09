# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Business-ISMN
Version:        1.205
Release:        %autorelease
Summary:        Work with International Standard Music Numbers
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Business-ISMN
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BR/BRIANDFOY/Business-ISMN-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Tie::Cycle) >= 1.21
BuildRequires:  perl(version) >= 0.86

Requires:       perl(Tie::Cycle) >= 1.21

%description
Methods

%prep
%setup -q -n Business-ISMN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes INSTALL.SKIP ismns.txt SECURITY.md

%changelog
%autochangelog
