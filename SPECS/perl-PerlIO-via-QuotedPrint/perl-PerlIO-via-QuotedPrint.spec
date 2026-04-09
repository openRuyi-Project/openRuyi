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
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SH/SHAY/PerlIO-via-QuotedPrint-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
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

%prep
%setup -q -n PerlIO-via-QuotedPrint-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
