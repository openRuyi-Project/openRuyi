# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tar_name SGMLSpm

Name:           perl-SGMLSpm
Version:        1.1
Release:        %autorelease
Summary:        SGMLSpm Perl module
License:        GPL-2.0-or-later
URL:            https://metacpan.org/dist/SGMLSpm
#!RemoteAsset:  sha256:550c9245291c8df2242f7e88f7921a0f636c7eec92c644418e7d89cfea70b2bd
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RAAB/SGMLSpm-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.

%files -f %{name}.files
%doc BUGS ChangeLog DOC elisp MYMETA.yml README script TODO

%changelog
%autochangelog
