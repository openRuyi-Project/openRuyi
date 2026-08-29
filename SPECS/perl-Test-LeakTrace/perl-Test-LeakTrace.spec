# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-LeakTrace
Version:        0.17
Release:        %autorelease
Summary:        Traces memory leaks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-LeakTrace
#!RemoteAsset:  sha256:777d64d2938f5ea586300eef97ef03eacb43d4c1853c9c3b1091eb3311467970
Source0:        https://www.cpan.org/authors/id/L/LE/LEEJO/Test-LeakTrace-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl-devel

Requires:       perl(Exporter) >= 5.57

%description
Test::LeakTrace provides several functions that trace memory leaks. This
module scans arenas, the memory allocation system, so it can detect any
leaked SVs in given blocks.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
