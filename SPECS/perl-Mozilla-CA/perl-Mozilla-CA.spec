# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Mozilla-CA
Version:        20250602
Release:        %autorelease
Summary:        Mozilla's CA cert bundle in PEM format
License:        MPL-2.0
URL:            https://metacpan.org/dist/Mozilla-CA
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/L/LW/LWP/Mozilla-CA-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.94

%description
Mozilla::CA provides a copy of Mozilla's bundle of Certificate Authority
certificates in a form that can be consumed by modules and libraries based
on OpenSSL.

%prep
%setup -q -n Mozilla-CA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes maint README

%changelog
%autochangelog
