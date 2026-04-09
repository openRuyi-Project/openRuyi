# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-libwww-perl
Version:        6.80
Release:        %autorelease
Summary:        libwww::perl Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/libwww-perl
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/O/OA/OALDERS/libwww-perl-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Listing) >= 6
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser) >= 3.71
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(HTTP::Cookies) >= 6
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Negotiate) >= 6
BuildRequires:  perl(HTTP::Request) >= 6.18
BuildRequires:  perl(HTTP::Request::Common) >= 6.18
BuildRequires:  perl(HTTP::Response) >= 6.18
BuildRequires:  perl(HTTP::Status) >= 6.18
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(MIME::Base64) >= 2.1
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Net::FTP) >= 2.58
BuildRequires:  perl(Net::HTTP) >= 6.18
BuildRequires:  perl(parent) >= 0.217
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
BuildRequires:  perl(WWW::RobotRules) >= 6

Requires:       perl(Encode) >= 2.12
Requires:       perl(File::Listing) >= 6
Requires:       perl(HTML::HeadParser) >= 3.71
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Negotiate) >= 6
Requires:       perl(HTTP::Request) >= 6.18
Requires:       perl(HTTP::Request::Common) >= 6.18
Requires:       perl(HTTP::Response) >= 6.18
Requires:       perl(HTTP::Status) >= 6.18
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(MIME::Base64) >= 2.1
Requires:       perl(Net::FTP) >= 2.58
Requires:       perl(Net::HTTP) >= 6.18
Requires:       perl(parent) >= 0.217
Requires:       perl(URI) >= 1.10
Requires:       perl(WWW::RobotRules) >= 6

%description
As of libwww-perl v6.02 you need to install the LWP::Protocol::https module
from its own separate distribution to enable support for https://... URLs
for LWP::UserAgent.

%prep
%setup -q -n libwww-perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes codecov.yml CONTRIBUTING.md perlimports.toml README.SSL talk-to-ourself

%changelog
%autochangelog
