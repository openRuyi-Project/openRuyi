# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Archive-Tar
Version:        3.04
Release:        %autorelease
Summary:        Module for manipulations of tar archives
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Archive-Tar
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.5.30
BuildRequires:  perl(Compress::Zlib) >= 2.015
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(IO::Compress::Base) >= 2.015
BuildRequires:  perl(IO::Compress::Bzip2) >= 2.015
BuildRequires:  perl(IO::Compress::Gzip) >= 2.015
BuildRequires:  perl(IO::Compress::Xz)
BuildRequires:  perl(IO::Uncompress::UnXz)
BuildRequires:  perl(IO::Zlib) >= 1.01
BuildRequires:  perl(Test::Harness) >= 2.26
BuildRequires:  perl(Test::More)

Requires:       perl(Compress::Zlib) >= 2.015
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(IO::Compress::Base) >= 2.015
Requires:       perl(IO::Compress::Bzip2) >= 2.015
Requires:       perl(IO::Compress::Gzip) >= 2.015
Requires:       perl(IO::Zlib) >= 1.01
Requires:       perl(Test::Harness) >= 2.26

%description
Archive::Tar provides an object oriented mechanism for handling tar files.
It provides class methods for quick and easy files handling while also
allowing for the creation of tar file objects for custom manipulation. If
you have the IO::Zlib module installed, Archive::Tar will also support
compressed or gzipped tar files.

%prep
%setup -q -n Archive-Tar-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
