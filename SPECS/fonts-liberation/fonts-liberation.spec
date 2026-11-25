# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-liberation
Version:        2.1.5
Release:        %autorelease
Summary:        Metrically compatible sans-serif, serif and monospace fonts
License:        OFL-1.1-RFN
URL:            https://github.com/liberationfonts/liberation-fonts
#!RemoteAsset:  sha256:fb22c2109dcbb25202aeb6202c0a58fd2e536dbf7c72879c4bbfa2b8a9a75d60
Source0:        %{url}/files/7261483/liberation-fonts-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(prep):  -n liberation-fonts-%{version}
BuildOption(build):  PYTHON=%{python3}

BuildRequires:  fontforge
BuildRequires:  fonts-rpm-macros
BuildRequires:  make
BuildRequires:  python3dist(fonttools)
BuildRequires:  pkgconfig(python3)

Requires:       %{name}-mono = %{version}-%{release}
Requires:       %{name}-sans = %{version}-%{release}
Requires:       %{name}-serif = %{version}-%{release}

%description
The Liberation typefaces preserve the character widths of Arial, Times New
Roman and Courier New. This package installs all three font families.

%package        mono
Summary:        Monospace fonts metrically compatible with Courier New

%description    mono
Liberation Mono provides regular, italic, bold and bold italic faces for
fixed-width text.

%package        sans
Summary:        Sans-serif fonts metrically compatible with Arial

%description    sans
Liberation Sans provides regular, italic, bold and bold italic sans-serif
faces for documents and user interfaces.

%package        serif
Summary:        Serif fonts metrically compatible with Times New Roman

%description    serif
Liberation Serif provides regular, italic, bold and bold italic serif
faces for typeset documents.

# The upstream Makefile builds the SFD sources directly with FontForge.
%conf

%install
%install_fonts liberation-fonts-ttf-%{version}/LiberationMono-*.ttf liberation-mono
%install_fonts liberation-fonts-ttf-%{version}/LiberationSans-*.ttf liberation-sans
%install_fonts liberation-fonts-ttf-%{version}/LiberationSerif-*.ttf liberation-serif

%files
%doc README.md
%license LICENSE

%files mono
%license LICENSE
%font_files liberation-mono ttf

%files sans
%license LICENSE
%font_files liberation-sans ttf

%files serif
%license LICENSE
%font_files liberation-serif ttf

%changelog
%autochangelog
