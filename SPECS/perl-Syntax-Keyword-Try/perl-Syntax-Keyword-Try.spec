# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Syntax-Keyword-Try
Version:        0.31
Release:        %autorelease
Summary:        Try/catch/finally syntax for perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Syntax-Keyword-Try
#!RemoteAsset:  sha256:7bc6242d746378982a599b34de35f07d3decc9e09d5646f8fa3b87f459414a4a
Source0:        https://www.cpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Try-%{version}.tar.gz
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor optimize="%{optflags}"
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.14.0
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(XS::Parse::Keyword) >= 0.35

Requires:       perl(XS::Parse::Keyword) >= 0.35

%description
This module provides a syntax plugin that implements exception-handling
semantics in a form familiar to users of other languages, being built on a
block labeled with the try keyword, followed by at least one of a catch or
finally block.

%files -f %{name}.files
%doc Changes README hax

%changelog
%autochangelog
