# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-PadWalker
Version:        2.5
Release:        %autorelease
Summary:        Play with other peoples' lexical variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/PadWalker
#!RemoteAsset:  sha256:07b26abb841146af32072a8d68cb90176ffb176fd9268e6f2f7d106f817a0cd0
Source0:        https://www.cpan.org/authors/id/R/RO/ROBIN/PadWalker-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
PadWalker is a module which allows you to inspect (and even change!)
lexical variables in any subroutine which called you. It will only show
those variables which are in scope at the point of the call.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
