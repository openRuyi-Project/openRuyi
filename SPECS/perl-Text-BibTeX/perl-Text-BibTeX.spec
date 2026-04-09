# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-BibTeX
Version:        0.91
Release:        %autorelease
Summary:        Interface to read and parse BibTeX files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-BibTeX
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/A/AM/AMBS/Text-BibTeX-%{version}.tar.gz

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.06
BuildRequires:  perl(Config::AutoConf) >= 0.320
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.02
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util) >= 1.42
BuildRequires:  perl(Unicode::Normalize)

Requires:       perl(Scalar::Util) >= 1.42

%description
The Text::BibTeX module serves mainly as a high-level introduction to the
Text::BibTeX library, for both code and documentation purposes. The code
loads the two fundamental modules for processing BibTeX files
(Text::BibTeX::File and Text::BibTeX::Entry), and this documentation gives
a broad overview of the whole library that isn't available in the
documentation for the individual modules that comprise it.

%prep
%setup -q -n Text-BibTeX-%{version}

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc btparse Changes examples README README.OLD scripts THANKS xscode
%{_includedir}/btparse.h
%{_libdir}/libbtparse.so

%changelog
%autochangelog
