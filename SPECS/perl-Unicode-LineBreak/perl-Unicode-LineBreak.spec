# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Unicode-LineBreak
Version:        2019.001
Release:        %autorelease
Summary:        UAX #14 Unicode Line Breaking Algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Unicode-LineBreak
#!RemoteAsset:  sha256:486762e4cacddcc77b13989f979a029f84630b8175e7fef17989e157d4b6318a
Source0:        https://www.cpan.org/authors/id/N/NE/NEZUMI/Unicode-LineBreak-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Encode) >= 1.98
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Charset) >= 1.6.2
BuildRequires:  perl(Test::More) >= 0.45

Requires:       perl(Encode) >= 1.98
Requires:       perl(MIME::Charset) >= 1.6.2

%description
Unicode::LineBreak performs Line Breaking Algorithm described in Unicode
Standard Annex #14 [UAX #14]. East_Asian_Width informative property defined
by Annex #11 [UAX #11] will be concerned to determine breaking positions.

%files -f %{name}.files
%doc ARTISTIC Changes Changes.REL1 Makefile.PL.sombok README Todo.REL1 perl-Unicode-LineBreak.spec

%changelog
%autochangelog
