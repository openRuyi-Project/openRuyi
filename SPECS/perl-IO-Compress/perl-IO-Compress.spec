# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Compress
Version:        2.220
Release:        %autorelease
Summary:        Read/write compressed data in multiple formats
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress
#!RemoteAsset:  sha256:9d96ea291f2c54ef367c7396b857d93ba1ac1c4b2f1bce13ed8a3e5f3eebb627
Source0:        https://www.cpan.org/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Bzip2) >= 2.218
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.218
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)

Requires:       perl(Compress::Raw::Bzip2) >= 2.218
Requires:       perl(Compress::Raw::Zlib) >= 2.218

# don't use cpan2spec's description.
%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.
IO-Compress supports reading and writing of bzip2, RFC 1950, RFC 1951,
RFC 1952 (i.e. gzip) and zip files/buffers.
This is a stub module. It contains no code.

# do not use buildsystem to install.
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
%doc Changes README SECURITY.md

%changelog
%autochangelog
