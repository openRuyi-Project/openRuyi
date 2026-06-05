# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Class-Tiny
Version:        1.008
Release:        %autorelease
Summary:        Minimalist class construction
License:        Apache-2.0
URL:            https://metacpan.org/dist/Class-Tiny
#!RemoteAsset:  sha256:ee058a63912fa1fcb9a72498f56ca421a2056dc7f9f4b67837446d6421815615
Source0:        https://www.cpan.org/authors/id/D/DA/DAGOLDEN/Class-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

%description
This module offers a minimalist class construction kit in around 120 lines
of code. Here is a list of features:

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README tidyall.ini

%changelog
%autochangelog
