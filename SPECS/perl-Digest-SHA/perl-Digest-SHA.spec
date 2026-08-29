# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Digest-SHA
Version:        6.04
Release:        %autorelease
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Digest-SHA
#!RemoteAsset:  sha256:ee91f8f7db894ee7c6ee003daac10a99056c4948a674ef46acdbb63c81a4abeb
Source0:        https://www.cpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.3.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel

%description
Digest::SHA is written in C for speed. If your platform lacks a C compiler,
you can install the functionally equivalent (but much slower)
Digest::SHA::PurePerl module.

%files -f %{name}.files
%doc Changes README shasum

%changelog
%autochangelog
