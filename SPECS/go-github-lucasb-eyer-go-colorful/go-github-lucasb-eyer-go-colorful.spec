# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-colorful
%define go_import_path  github.com/lucasb-eyer/go-colorful

Name:           go-github-lucasb-eyer-go-colorful
Version:        1.3.0
Release:        %autorelease
Summary:        A library for playing with colors in go (golang).
License:        MIT
URL:            https://github.com/lucasb-eyer/go-colorful
#!RemoteAsset
Source0:        https://github.com/lucasb-eyer/go-colorful/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lucasb-eyer/go-colorful) = %{version}

%description
A library for playing with colors in Go. Supports Go 1.13 onwards.

Go-Colorful stores colors in RGB and provides methods from converting
these to various color-spaces. Currently supported colorspaces are:

 * **RGB:** All three of Red, Green and Blue in [0..1].
 * **HSL:** Hue in [0..360], Saturation and Luminance in [0..1]. For
   legacy reasons; please forget that it exists.
 * **HSV:** Hue in [0..360], Saturation and Value in [0..1]. You're
   better off using HCL, see below.
 * **Hex RGB:** The "internet" color format, as in #FF00FF.
 * **Linear RGB:** See gamma correct rendering (http://www.sjbrown.co.
   uk/2004/05/14/gamma-correct-rendering/).
 * **CIE-XYZ:** CIE's standard color space, almost in [0..1].
 * **CIE-xyY:** encodes chromacity in x and y and luminance in Y, all in
   [0..1]
 * **CIE-L*a*b*:** A *perceptually uniform* color space, i.e. distances
   are meaningful. L* in [0..1] and a*, b* almost in [-1..1].
 * **CIE-L*u*v*:** Very similar to CIE-L*a*b*, there is no consensus
   (http://en.wikipedia.org/wiki/CIELUV#Historical_background) on which
   one is "better".
 * **CIE-L*C*h° (HCL):** This is generally the most useful (http://vis4.
   net/blog/posts/avoid-equidistant-hsv-colors/) one; CIE-L*a*b* space in
   polar coordinates, i.e. a *better* HSV. H° is in [0..360], C* almost in
   [0..1] and L* as in CIE-L*a*b*.
 * **CIE LCh(uv):** Called LuvLCh in code, this is a cylindrical
   transformation of the CIE-L*u*v* color space. Like HCL above: H° is in
   [0..360], C* almost in [0..1] and L* as in CIE-L*u*v*.
 * **HSLuv:** The better alternative to HSL, see here (https://www.hsluv.
   org/) and here (https://www.kuon.ch/post/2020-03-08-hsluv/). Hue in [0..
   360], Saturation and Luminance in [0..1].
 * **HPLuv:** A variant of HSLuv. The color space is smoother, but only
   pastel colors can be included. Because the valid colors are limited,
   it's easy to get invalid Saturation values way above 1.0, indicating
   the color can't be represented in HPLuv because it's not pastel.
 * **Oklab:** A perceptual color space by Björn Ottosson that improves
   on CIE-L*a*b* with better perceptual uniformity, especially for blue
   hues. L in [0..1], a and b roughly in [-0.5..0.5]. See Oklab
   (https://bottosson.github.io/posts/oklab/).
 * **Oklch:** The cylindrical (polar) representation of Oklab, similar
   to HCL. L in [0..1], C roughly in [0..0.5], h° in [0..360].

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
