# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Try-Tiny
Version:        0.32
Release:        %autorelease
Summary:        Minimal try/catch with proper preservation of $@
License:        MIT
URL:            https://metacpan.org/dist/Try-Tiny
#!RemoteAsset:  sha256:ef2d6cab0bad18e3ab1c4e6125cc5f695c7e459899f512451c8fa3ef83fa7fc0
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Try-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(Exporter) >= 5.57

%description
This module provides bare bones try/catch/finally statements that are
designed to minimize common mistakes with eval blocks, and NOTHING else.

%files -f %{name}.files
%doc Changes CONTRIBUTING maint README

%changelog
%autochangelog
