# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Data-Compare
Version:        1.29
Release:        %autorelease
Summary:        Compare perl data structures
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/dist/Data-Compare
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Clone) >= 0.43
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule) >= 0.1
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Clone) >= 0.43
Requires:       perl(File::Find::Rule) >= 0.1
Requires:       perl(Test::More) >= 0.88

%description
Compare two perl data structures recursively. Returns 0 if the structures
differ, else returns 1.

%prep
%setup -q -n Data-Compare-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGELOG MAINTAINERS-NOTE NOTES README

%changelog
%autochangelog
