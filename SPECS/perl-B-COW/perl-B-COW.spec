# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-B-COW
Version:        0.007
Release:        %autorelease
Summary:        B::COW additional B helpers to check COW status
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/B-COW
#!RemoteAsset:  sha256:1290daf227e8b09889a31cf182e29106f1cf9f1a4e9bf7752f9de92ed1158b44
Source0:        https://www.cpan.org/authors/id/A/AT/ATOOMIC/B-COW-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel

%description
B::COW provides some naive additional B helpers to check the COW status
  of one SvPV.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
