# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Perl-Critic
Version:        1.156
Release:        %autorelease
Summary:        Critique Perl source code for best-practices
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Perl-Critic
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.10.1
BuildRequires:  perl(B::Keywords) >= 1.23
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Config::Tiny) >= 2
BuildRequires:  perl(English)
BuildRequires:  perl(Exception::Class) >= 1.23
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::SomeUtils) >= 0.55
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable) >= 3.1
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(Pod::Spell) >= 1
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(PPI) >= 1.277
BuildRequires:  perl(PPI::Document) >= 1.277
BuildRequires:  perl(PPI::Document::File) >= 1.277
BuildRequires:  perl(PPI::Node) >= 1.277
BuildRequires:  perl(PPI::Token::Quote::Single) >= 1.277
BuildRequires:  perl(PPI::Token::Whitespace) >= 1.277
BuildRequires:  perl(PPIx::QuoteLike)
BuildRequires:  perl(PPIx::Regexp) >= 0.027
BuildRequires:  perl(PPIx::Regexp::Util) >= 0.068
BuildRequires:  perl(PPIx::Utils::Traversal) >= 0.003
BuildRequires:  perl(Readonly) >= 2
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Format) >= 1.18
BuildRequires:  perl(Term::ANSIColor) >= 2.02
BuildRequires:  perl(Test::Builder) >= 0.92
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords) >= 3
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
# Manual
BuildRequires:  perl(Try::Tiny)

Requires:       perl(B::Keywords) >= 1.23
Requires:       perl(Config::Tiny) >= 2
Requires:       perl(Exception::Class) >= 1.23
Requires:       perl(Exporter) >= 5.63
Requires:       perl(List::SomeUtils) >= 0.55
Requires:       perl(Module::Pluggable) >= 3.1
Requires:       perl(Pod::Spell) >= 1
Requires:       perl(PPI) >= 1.277
Requires:       perl(PPI::Document) >= 1.277
Requires:       perl(PPI::Document::File) >= 1.277
Requires:       perl(PPI::Node) >= 1.277
Requires:       perl(PPI::Token::Quote::Single) >= 1.277
Requires:       perl(PPI::Token::Whitespace) >= 1.277
Requires:       perl(PPIx::Regexp) >= 0.027
Requires:       perl(PPIx::Regexp::Util) >= 0.068
Requires:       perl(PPIx::Utils::Traversal) >= 0.003
Requires:       perl(Readonly) >= 2
Requires:       perl(String::Format) >= 1.18
Requires:       perl(Term::ANSIColor) >= 2.02
Requires:       perl(Test::Builder) >= 0.92
Requires:       perl(Text::ParseWords) >= 3
Requires:       perl(version) >= 0.77

%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code
analysis engine. Perl::Critic is distributed with a number of
Perl::Critic::Policy modules that attempt to enforce various coding
guidelines. Most Policy modules are based on Damian Conway's book Perl Best
Practices. However, Perl::Critic is not limited to PBP and will even
support Policies that contradict Conway. You can enable, disable, and
customize those Polices through the Perl::Critic interface. You can also
create new Policy modules that suit your own tastes.

%prep
%setup -q -n Perl-Critic-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md examples extras perlcriticrc README README.md tools xt

%changelog
%autochangelog
