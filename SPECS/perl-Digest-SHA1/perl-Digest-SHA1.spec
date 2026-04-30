# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Digest-SHA1
Version:        2.13
Release:        %autorelease
Summary:        Perl interface to the SHA-1 algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Digest-SHA1
#!RemoteAsset:  sha256:68c1dac2187421f0eb7abf71452a06f190181b8fc4b28ededf5b90296fb943cc
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-SHA1-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::base) >= 1.00
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Digest::base) >= 1.00

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message digest
algorithm from within Perl programs. The algorithm takes as input a message
of arbitrary length and produces as output a 160-bit "fingerprint" or
"message digest" of the input.

%prep
%setup -q -n Digest-SHA1-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%files -f %{name}.files
%doc Changes README fip180-1.gif fip180-1.html
%license
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*

%changelog
%autochangelog
