# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IPC-SysV
Version:        2.09
Release:        %autorelease
Summary:        System V IPC constants and system calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IPC-SysV
#!RemoteAsset:  sha256:1897541c74d548fd1007eb6c07f3419d3c7575d8056a62b5ba5270a2166d2dbd
Source0:        https://www.cpan.org/authors/id/M/MH/MHX/IPC-SysV-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl-devel

Requires:       perl(Test::More) >= 0.45

%description
IPC::SysV defines and conditionally exports all the constants defined in
your system include files which are needed by the SysV IPC calls. Common
ones include

%files -f %{name}.files
%doc Changes const-c.inc const-xs.inc README TODO

%changelog
%autochangelog
