# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tar_name SGMLSpm

Name:           perl-SGMLSpm
Version:        1.03ii
Release:        %autorelease
Summary:        Perl library for parsing the output of nsgmls
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/SGMLSpm
#!RemoteAsset
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMEGG/%{tar_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-macros

Requires:       openjade

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.

%prep
%setup -q -n SGMLSpm

%build
# Daddy no build

%install
install -d -m 755 $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}}
make install_system \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    PERL5DIR=$RPM_BUILD_ROOT%{perl_vendorlib}

%files
%doc README COPYING
%{_bindir}/sgmlspl
%{perl_vendorlib}/SGMLS*
%{perl_vendorlib}/skel.pl

%changelog
%autochangelog
