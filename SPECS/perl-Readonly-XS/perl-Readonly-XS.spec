# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Readonly-XS
Version:        1.05
Release:        %autorelease
Summary:        Companion module for Readonly.pm, to speed up read-only scalar variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Readonly-XS
#!RemoteAsset:  sha256:8ae5c4e85299e5c8bddd1b196f2eea38f00709e0dc0cb60454dc9114ae3fff0d
Source0:        https://www.cpan.org/authors/id/R/RO/ROODE/Readonly-XS-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Readonly) >= 1.02
BuildRequires:  perl-devel

Requires:       perl(Readonly) >= 1.02

%description
The Readonly module (q.v.) is an effective way to create non-modifiable
variables. However, it's relatively slow.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
