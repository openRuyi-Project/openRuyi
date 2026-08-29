# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-PerlIO-via-QuotedPrint
Version:        0.10
Release:        %autorelease
Summary:        PerlIO layer for quoted-printable strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/PerlIO-via-QuotedPrint
#!RemoteAsset:  sha256:3ec4d3e0d7dd64f7fef21e788f67646f68c3abe28d75e6ebe020d2ef4e22b949
Source0:        https://www.cpan.org/authors/id/S/SH/SHAY/PerlIO-via-QuotedPrint-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)

%description
This module implements a PerlIO layer that works on files encoded in the
quoted-printable format. It will decode from quoted-printable while
reading from a handle, and it will encode as quoted-printable while
writing to a handle.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
