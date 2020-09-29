/*
 * Copyright (C) 2020 Anonymous
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
package io.github.anonymous.miners

import io.github.anonymous.detectors.ElkiLOF
import io.github.anonymous.mcde.KSP
import io.github.anonymous.searchers.{GMD, SubspaceSearcher}

/**
  * Created by anonymous.
  */
case class GMDOutlierMiner(k: Int = 100, max1000: Boolean = true) extends SubspaceOutlierMiner {
  val subspaceSearcher: SubspaceSearcher = GMD(KSP())
  val detector = ElkiLOF(k)
  val id = subspaceSearcher.id + "-" + detector.id + "-" + s"$max1000"(0)
}
