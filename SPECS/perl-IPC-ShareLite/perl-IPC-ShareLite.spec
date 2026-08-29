# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IPC-ShareLite
Version:        0.17
Release:        %autorelease
Summary:        Lightweight interface to shared memory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IPC-ShareLite
#!RemoteAsset:  sha256:14d406b91da96d6521d0d1a82d22a306274765226b86b0a56e7ffddcf96ae7bf
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDYA/IPC-ShareLite-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%description
IPC::ShareLite provides a simple interface to shared memory, allowing
data to be efficiently communicated between processes. Your operating
system must support SysV IPC (shared memory and semaphores) in order to
use this module.

%files -f %{name}.files
%doc Changes README
%license
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IPC*

%changelog
%autochangelog
