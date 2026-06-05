# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-common-sense
Version:        3.75
Release:        %autorelease
Summary:        Save a tree AND a kitten, use common::sense!
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/common-sense
#!RemoteAsset:  sha256:a86a1c4ca4f3006d7479064425a09fa5b6689e57261fcb994fe67d061cba0e7e
Source0:        https://www.cpan.org/authors/id/M/ML/MLEHMANN/common-sense-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
“Nothing is more fairly distributed than common sense: no one thinks   he
needs more of it than he already has.”

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
