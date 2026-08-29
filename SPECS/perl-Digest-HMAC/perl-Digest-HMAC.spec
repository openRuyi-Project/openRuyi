# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Digest-HMAC
Version:        1.05
Release:        %autorelease
Summary:        Keyed-Hashing for Message Authentication
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Digest-HMAC
#!RemoteAsset:  sha256:215cb59cba610745cfb2d4b3f8ef756d590e57e3ad7986a992e87c4969fcdc7a
Source0:        https://www.cpan.org/authors/id/A/AR/ARODLAND/Digest-HMAC-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Digest::MD5) >= 2
BuildRequires:  perl(Digest::SHA) >= 1
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:       perl(Digest::MD5) >= 2
Requires:       perl(Digest::SHA) >= 1

%description
HMAC is used for message integrity checks between two parties that share a
secret key, and works in combination with some other Digest algorithm,
usually MD5 or SHA-1. The HMAC mechanism is described in RFC 2104.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
