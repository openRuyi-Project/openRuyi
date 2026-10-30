# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Logfile-Rotate
Version:        1.04
Release:        %autorelease
Summary:        Perl module to rotate log files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Logfile-Rotate
# VCS: No VCS link available
#!RemoteAsset:  sha256:810f8b7ccd8657d3b1ef53cd47582547845cebb58202b05539b3408638cada3e
Source0:        https://www.cpan.org/authors/id/P/PA/PAULG/Logfile-Rotate-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy) >= 2.02

Recommends:     gzip
Requires:       perl(File::Copy) >= 2.02

%description
Logfile::Rotate is a Perl module that rotates log files, optionally
compressing and moving the rotated files.

%files -f %{name}.files
%doc Changes Logfile-Rotate.man.html README TODO

%changelog
%autochangelog
