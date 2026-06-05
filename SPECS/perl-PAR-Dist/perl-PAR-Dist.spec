# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-PAR-Dist
Version:        0.53
Release:        %autorelease
Summary:        Create and manipulate PAR distributions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/PAR-Dist
#!RemoteAsset:  sha256:04cbc81e786968f9a4109ad6c2f9b81e879ac0c6b6080a9d217443b61dfd2498
Source0:        https://www.cpan.org/authors/id/R/RS/RSCHUPP/PAR-Dist-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

%description
This module creates and manipulates PAR distributions. They are architecture-
specific PAR files, containing everything under blib/ of CPAN distributions
after their make or Build stage, a META.yml describing metadata of the
original CPAN distribution, and a MANIFEST detailing all files within it.
Digitally signed PAR distributions will also contain a SIGNATURE file.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
