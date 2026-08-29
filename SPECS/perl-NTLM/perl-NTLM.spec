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
#!RemoteAsset:  sha256:c823e30cda76bc15636e584302c960e2b5eeef9517c2448f7454498893151f85
Source0:        https://www.cpan.org/authors/id/N/NB/NBEBOUT/NTLM-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)

%description
This module provides methods to use NTLM authentication.  It can    be used
as an authenticate method with the Mail::IMAPClient module    to perform
the challenge/response mechanism for NTLM connections    or it can be used
on its own for NTLM authentication with other    protocols (eg. HTTP).

%files -f %{name}.files
%doc Changes COPYING-Artistic COPYING-GPL README

%changelog
%autochangelog
