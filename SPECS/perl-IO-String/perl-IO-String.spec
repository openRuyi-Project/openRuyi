# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-String
Version:        1.08
Release:        %autorelease
Summary:        Emulate file interface for in-core strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-String
#!RemoteAsset:  sha256:2a3f4ad8442d9070780e58ef43722d19d1ee21a803bf7c8206877a10482de5a0
Source0:        https://www.cpan.org/authors/id/G/GA/GAAS/IO-String-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
The IO::String module provides the IO::File interface for in-core strings.
An IO::String object can be attached to a string, and makes it possible to
use the normal file operations for reading or writing data, as well as for
seeking to various locations of the string. This is useful when you want to
use a library module that only provides an interface to file handles on
data that you have in a string variable.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
