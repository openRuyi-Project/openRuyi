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
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RS/RSCHUPP/PAR-Dist-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
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

%prep
%setup -q -n PAR-Dist-%{version}

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
