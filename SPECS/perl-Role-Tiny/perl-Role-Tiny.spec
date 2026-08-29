# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Role-Tiny
Version:        2.002005
Release:        %autorelease
Summary:        Roles: a nouvelle cuisine portion size slice of Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Role-Tiny
#!RemoteAsset:  sha256:4618ec524618c104dc28a8cc86af129a00cad282aea7f4c75060ba05d4c8f4d7
Source0:        https://www.cpan.org/authors/id/H/HA/HAARG/Role-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Class::Method::Modifiers) >= 1.05
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Class::Method::Modifiers) >= 1.05

%description
Role::Tiny is a minimalist role composition tool.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
