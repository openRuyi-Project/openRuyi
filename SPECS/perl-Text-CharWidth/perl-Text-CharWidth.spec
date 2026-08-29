# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-CharWidth
Version:        0.04
Release:        %autorelease
Summary:        Get number of occupied columns of a string on terminal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-CharWidth
#!RemoteAsset:  sha256:abded5f4fdd9338e89fd2f1d8271c44989dae5bf50aece41b6179d8e230704f8
Source0:        https://www.cpan.org/authors/id/K/KU/KUBOTA/Text-CharWidth-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module supplies features similar as wcwidth(3) and wcswidth(3) in
C language.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
