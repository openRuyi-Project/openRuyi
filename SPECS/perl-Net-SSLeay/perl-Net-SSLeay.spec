# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Net-SSLeay
Version:        1.94
Release:        %autorelease
Summary:        Perl bindings for OpenSSL and LibreSSL
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Net-SSLeay
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.60_01
# Manual
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
This module provides Perl bindings for libssl (an SSL/TLS API) and
libcrypto (a cryptography API).

%prep
%setup -q -n Net-SSLeay-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md Credits QuickRef README README.OSX README.VMS README.Win32

%changelog
%{?autochangelog}
