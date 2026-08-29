# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Compress-Lzma
Version:        2.217
Release:        %autorelease
Summary:        Write lzma files/buffers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress-Lzma
#!RemoteAsset:  sha256:3462ecd1e67e85d5e4fa911bc6d8e38a884ba1d6e90a03535f0d28fe2ad0aacf
Source0:        https://www.cpan.org/authors/id/P/PM/PMQS/IO-Compress-Lzma-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Lzma) >= 2.217
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Compress::Base) >= 2.217
BuildRequires:  perl(IO::Uncompress::Base) >= 2.217

Requires:       perl(Compress::Raw::Lzma) >= 2.217
Requires:       perl(IO::Compress::Base) >= 2.217
Requires:       perl(IO::Uncompress::Base) >= 2.217

%description
This module provides a Perl interface that allows writing lzma compressed
data to files or buffer.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
