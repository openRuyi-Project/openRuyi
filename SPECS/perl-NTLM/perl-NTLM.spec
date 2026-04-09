# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-NTLM
Version:        1.09
Release:        %autorelease
Summary:        NTLM Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/NTLM
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/N/NB/NBEBOUT/NTLM-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)

%description
This module provides methods to use NTLM authentication.  It can    be used
as an authenticate method with the Mail::IMAPClient module    to perform
the challenge/response mechanism for NTLM connections    or it can be used
on its own for NTLM authentication with other    protocols (eg. HTTP).

%prep
%setup -q -n NTLM-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes COPYING-Artistic COPYING-GPL README

%changelog
%autochangelog
