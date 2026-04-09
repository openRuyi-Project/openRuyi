# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Compress-Lzma
Version:        2.214
Release:        %autorelease
Summary:        Write lzma files/buffers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress-Lzma
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PM/PMQS/IO-Compress-Lzma-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Lzma) >= 2.214
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Compress::Base) >= 2.214
BuildRequires:  perl(IO::Uncompress::Base) >= 2.214

Requires:       perl(Compress::Raw::Lzma) >= 2.214
Requires:       perl(IO::Compress::Base) >= 2.214
Requires:       perl(IO::Uncompress::Base) >= 2.214

%description
This module provides a Perl interface that allows writing lzma compressed
data to files or buffer.

%prep
%setup -q -n IO-Compress-Lzma-%{version}

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
