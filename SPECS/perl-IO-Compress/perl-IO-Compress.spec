# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Compress
Version:        2.214
Release:        %autorelease
Summary:        Read/write compressed data in multiple formats
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Bzip2) >= 2.214
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.214
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)

Requires:       perl(Compress::Raw::Bzip2) >= 2.214
Requires:       perl(Compress::Raw::Zlib) >= 2.214

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.
IO-Compress supports reading and writing of bzip2, RFC 1950, RFC 1951,
RFC 1952 (i.e. gzip) and zip files/buffers.

%prep
%setup -q -n IO-Compress-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
# Avoid file conflicts with perl core
mv %{buildroot}/usr/bin/streamzip %{buildroot}/usr/bin/streamzip-%{version}
mv %{buildroot}/usr/bin/zipdetails %{buildroot}/usr/bin/zipdetails-%{version}
mv %{buildroot}/usr/share/man/man1/streamzip.1perl %{buildroot}/usr/share/man/man1/streamzip-%{version}.1perl
mv %{buildroot}/usr/share/man/man1/zipdetails.1perl %{buildroot}/usr/share/man/man1/zipdetails-%{version}.1perl
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
