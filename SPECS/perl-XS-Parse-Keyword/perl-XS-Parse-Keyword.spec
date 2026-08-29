# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XS-Parse-Keyword
Version:        0.49
Release:        %autorelease
Summary:        XS functions to assist in parsing keyword syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XS-Parse-Keyword
#!RemoteAsset:  sha256:76c5ed142abba1f1df2335849681c83d83cc0842fe854af71081d2c411efb0bb
Source0:        https://www.cpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-%{version}.tar.gz
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor optimize="%{optflags}"
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.14.0
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.16
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::V0)

Requires:       perl(File::ShareDir) >= 1.00

%description
This module provides some XS functions to assist in writing syntax modules
that provide new perl-visible syntax, primarily for authors of keyword
plugins using the PL_keyword_plugin hook mechanism. It is unlikely to be of
much use to anyone else; and highly unlikely to be any use when writing
perl code using these. Unless you are writing a keyword plugin using XS,
this module is not for you.

%files -f %{name}.files
%doc Changes README hax share-infix share-keyword src

%changelog
%autochangelog
