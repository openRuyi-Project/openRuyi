# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           natsort
%define go_import_path  github.com/facette/natsort
%define commit_id 2cd4dd1e2dcba4d85d6d3ead4adf4cfd2b70caf2

Name:           go-github-facette-natsort
Version:        0+git20181210.2cd4dd1
Release:        %autorelease
Summary:        Natural strings sorting in Go
License:        BSD-3-Clause
URL:            https://github.com/facette/natsort
#!RemoteAsset:  sha256:182e6dc9a313095acb504b30651b569a8b8410ef3e48120be6e1af39fe7ce7a5
Source0:        https://github.com/facette/natsort/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/facette/natsort) = %{version}


%description
natsort: natural strings sorting in Go

This is an implementation of the "Alphanum Algorithm" by Dave Koelle
(http://davekoelle.com/alphanum.html) in Go.

[Image: GoDoc] (https://godoc.org/facette.io/natsort?status.svg)
(https://godoc.org/facette.io/natsort)

Usage

  package main

  import (
      "fmt"
      "strings"

      "facette.io/natsort"
  )

  func main() {
      list := []string{
          "1000X Radonius Maximus",
          "10X Radonius",
          "200X Radonius",
          "20X Radonius",
          "20X Radonius Prime",
          "30X Radonius",
          "40X Radonius",
          "Allegia 50 Clasteron",
          "Allegia 500 Clasteron",
          "Allegia 50B Clasteron",
          "Allegia 51 Clasteron",
          "Allegia 6R Clasteron",
          "Alpha 100",
          "Alpha 2",
          "Alpha 200",
          "Alpha 2A",
          "Alpha 2A-8000",
          "Alpha 2A-900",
          "Callisto Morphamax",
          "Callisto Morphamax 500",
          "Callisto Morphamax 5000",
          "Callisto Morphamax 600",
          "Callisto Morphamax 6000 SE",
          "Callisto Morphamax 6000 SE2",
          "Callisto Morphamax 700",
          "Callisto Morphamax 7000",
          "Xiph Xlater 10000",
          "Xiph Xlater 2000",
          "Xiph Xlater 300",
          "Xiph Xlater 40",
          "Xiph Xlater 5",
          "Xiph Xlater 50",
          "Xiph Xlater 500",
          "Xiph Xlater 5000",
          "Xiph Xlater 58",
      }

      natsort.Sort(list)

      fmt.Println(strings.Join(list, "\n"))
  }

Output:

  10X Radonius
  20X Radonius
  20X Radonius Prime
  30X Radonius
  40X Radonius
  200X Radonius
  1000X Radonius Maximus
  Allegia 6R Clasteron
  Allegia 50 Clasteron
  Allegia 50B Clasteron
  Allegia 51 Clasteron
  Allegia 500 Clasteron
  Alpha 2
  Alpha 2A
  Alpha 2A-900
  Alpha 2A-8000
  Alpha 100
  Alpha 200
  Callisto Morphamax
  Callisto Morphamax 500
  Callisto Morphamax 600
  Callisto Morphamax 700
  Callisto Morphamax 5000
  Callisto Morphamax 6000 SE
  Callisto Morphamax 6000 SE2
  Callisto Morphamax 7000
  Xiph Xlater 5
  Xiph Xlater 40
  Xiph Xlater 50
  Xiph Xlater 58
  Xiph Xlater 300
  Xiph Xlater 500
  Xiph Xlater 2000
  Xiph Xlater 5000
  Xiph Xlater 10000


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
