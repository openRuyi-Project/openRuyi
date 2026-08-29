# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTML-Tagset
Version:        3.24
Release:        %autorelease
Summary:        Data tables useful in parsing HTML
License:        Artistic-2.0
URL:            https://metacpan.org/dist/HTML-Tagset
#!RemoteAsset:  sha256:eb89e145a608ed1f8f141a57472ee5f69e67592a432dcd2e8b1dbb445f2b230b
Source0:        https://www.cpan.org/authors/id/P/PE/PETDANCE/HTML-Tagset-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.95

%description
This module contains several data tables useful in various kinds of HTML
parsing operations.

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
