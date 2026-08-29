# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Data-UUID
Version:        1.227
Release:        %autorelease
Summary:        Globally/Universally Unique Identifiers (GUIDs/UUIDs)
# Makefile.PL says BSD but LICENSE file is HP-1989
# LICENSE: HP-1989
# source/ptable.h: GPL-1.0-or-later OR Artistic-1.0-Perl
# Issue for license clarification
# https://github.com/bleargh45/Data-UUID/issues/26
License:        HP-1989 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/Data-UUID
#!RemoteAsset:  sha256:95bda7276265f57bc48ffdeddec5ef28cd6f765e3a183757fa5f09f0ce6b98ac
Source0:        https://www.cpan.org/authors/id/G/GT/GTERMARS/Data-UUID-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel

%description
This module provides a framework for generating v3 UUIDs (Universally
Unique Identifiers, also known as GUIDs (Globally Unique Identifiers). A
UUID is 128 bits long, and is guaranteed to be different from all other
UUIDs/GUIDs generated until 3400 CE.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
