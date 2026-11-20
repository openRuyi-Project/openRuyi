// SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
// SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
//
// SPDX-License-Identifier: Apache-2.0

// kubecomps-package-chart packages a Helm chart with the Helm library already
// vendored by kubecomps. It avoids requiring a separate Helm binary during an
// offline distribution build.
package main

import (
	"fmt"
	"os"

	"helm.sh/helm/v3/pkg/action"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Fprintf(os.Stderr, "usage: %s CHART_DIR DESTINATION\n", os.Args[0])
		os.Exit(2)
	}

	pkg := action.NewPackage()
	pkg.Destination = os.Args[2]
	name, err := pkg.Run(os.Args[1], nil)
	if err != nil {
		fmt.Fprintf(os.Stderr, "package %s: %v\n", os.Args[1], err)
		os.Exit(1)
	}
	fmt.Println(name)
}
